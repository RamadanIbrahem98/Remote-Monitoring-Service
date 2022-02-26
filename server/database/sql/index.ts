import path from 'path';
import { Database, open as sqliteOpen } from 'sqlite';
import sqlite3 from 'sqlite3';
import { Datastore } from '..';
import { Reading, Temp, humidity } from '../../types';

export class sqlDatabase implements Datastore {
  private db!: Database<sqlite3.Database, sqlite3.Statement>;

  async openDb() {
    this.db = await sqliteOpen({
      filename: path.join(__dirname, 'sensors.sqlite'),
      driver: sqlite3.Database,
    });

    await this.db.migrate({
      migrationsPath: path.join(__dirname, '../migrations'),
    });

    return this;
  }

  async createSensorEntry(reading: Reading): Promise<void> {
    await this.db.run(
      'INSERT INTO readings (timestamp, temperature, humidity) VALUES (?,?,?)',
      reading.timestamp,
      reading.temperature,
      reading.humidity,
    );
  }

  async getTemperatures(timestamp: number): Promise<Temp[] | undefined> {
    const result = [{ timestamp: '', temperature: 0 }];
    await this.db.each(
      'SELECT timestamp, temperature FROM readings WHERE timestamp > ? ORDER BY timestamp ASC',
      timestamp,
      (err, row) => {
        if (err) {
          throw err;
        }

        result.push(row);
      },
    );

    return result.length > 1 ? result.slice(1) : undefined;
  }

  async getHumedities(timestamp: number): Promise<humidity[] | undefined> {
    const result = [{ timestamp: '', humidity: 0 }];
    await this.db.each(
      'SELECT timestamp, humidity FROM readings WHERE timestamp > ? ORDER BY timestamp ASC',
      timestamp,
      (err, row) => {
        if (err) {
          throw err;
        }

        result.push(row);
      },
    );

    return result.length > 1 ? result.slice(1) : undefined;
  }

  async purge(): Promise<void> {
    await this.db.run('DELETE FROM readings');
  }

  async setAlarm(is_set: number): Promise<void> {
    await this.db.run('UPDATE alarm SET is_set = ?', is_set);
  }

  async getAlarm(): Promise<number> {
    const res = await this.db.get('SELECT is_set FROM alarm WHERE id = 1');
    return res.is_set;
  }
}
