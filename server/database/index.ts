import { ReadingDao } from './dao/ReadingDao';

import { sqlDatabase } from './sql';

export interface Datastore extends ReadingDao {}

export let db: Datastore;

export async function initDb() {
  db = await new sqlDatabase().openDb();
}
