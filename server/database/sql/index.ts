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

  async getTemperatures(): Promise<Temp[] | undefined> {
    const result = [{ timestamp: '', temperature: 0 }];
    await this.db.each(
      'SELECT timestamp, temperature FROM readings ORDER BY timestamp DESC LIMIT 100',
      (err, row) => {
        if (err) {
          throw err;
        }

        result.push(row);
      },
    );

    return result.length > 1 ? result.slice(1) : undefined;
  }

  async getHumedities(): Promise<humidity[] | undefined> {
    const result = [{ timestamp: '', humidity: 0 }];
    await this.db.each(
      'SELECT timestamp, humidity FROM readings ORDER BY timestamp DESC LIMIT 100',
      (err, row) => {
        if (err) {
          throw err;
        }

        result.push(row);
      },
    );

    return result.length > 1 ? result.slice(1) : undefined;
  }
}
