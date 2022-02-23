import { Reading, Temp, humidity } from '../../types';

export interface ReadingDao {
  createSensorEntry(reading: Reading): Promise<void>;
  getTemperatures(timestamp: number): Promise<Temp[] | undefined>;
  getHumedities(timestamp: number): Promise<humidity[] | undefined>;
  purge(): Promise<void>;
}
