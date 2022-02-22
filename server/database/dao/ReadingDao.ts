import { Reading, Temp, humidity } from '../../types';

export interface ReadingDao {
  createSensorEntry(reading: Reading): Promise<void>;
  getTemperatures(): Promise<Temp[] | undefined>;
  getHumedities(): Promise<humidity[] | undefined>;
  purge(): Promise<void>;
}
