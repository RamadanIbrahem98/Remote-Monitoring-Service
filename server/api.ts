import { Temp, humidity } from './types';

export interface GetTempRequest {}
export interface GetTempResponse {
  temperatures: Temp[];
}

export interface GetHumidityRequest {}
export interface GetHumidityResponse {
  humidities: humidity[];
}

export interface CreateEntryRequest {
  timestamp: string;
  temperature: number;
  humidity: number;
}
export interface CreateEntryResponse {}

export interface EmptyRequest {}
