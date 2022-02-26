import { Temp, humidity } from './types';

export interface GetTempRequest {
  timestamp: number;
}
export interface GetTempResponse {
  temperatures: Temp[];
}

export interface GetHumidityRequest {
  timestamp: number;
}
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

export interface AlarmRequest {
  is_set: number;
}

export interface AlarmResponse {
  alarm: number;
}
