import sqlite3 from 'sqlite3';
import { open as sqliteOpen } from 'sqlite';
import path from 'path';

async function openDb() {
  const db = await sqliteOpen({
    filename: path.join(__dirname, 'sensors.sqlite'),
    driver: sqlite3.Database,
  });

  await db.migrate({
    migrationsPath: path.join(__dirname, 'migrations'),
  });

  return this;
}

export async function initDb() {
  db = await openDb();
}
