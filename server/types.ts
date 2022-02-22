import { RequestHandler } from 'express';

export interface Reading {
  timestamp: string;
  temperature: number;
  humidity: number;
}

export interface Temp {
  timestamp: string;
  temperature: number;
}

export interface humidity {
  timestamp: string;
  humidity: number;
}

export type ExpressHandler<Req, Res> = RequestHandler<
  string,
  Partial<Res>,
  Partial<Req>,
  any
>;
