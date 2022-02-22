import {
  GetTempRequest,
  GetTempResponse,
  GetHumidityRequest,
  GetHumidityResponse,
  CreateEntryRequest,
  CreateEntryResponse,
} from '../api';
import { db } from '../database';
import { ExpressHandler, Reading, Temp, humidity } from '../types';

export const newEntryHandler: ExpressHandler<
  CreateEntryRequest,
  CreateEntryResponse
> = async (req, res) => {
  const { timestamp, temperature, humidity } = req.body;
  if (!timestamp || !temperature || !humidity) {
    return res.status(400).json({
      message: 'Missing required fields',
    });
  }
  const reading: Reading = {
    timestamp,
    temperature,
    humidity,
  };
  await db.createSensorEntry(reading);

  return res.status(200).json({
    success: true,
  });
};

export const getTempHandler: ExpressHandler<
  GetTempRequest,
  GetTempResponse
> = async (req, res) => {
  const temperatures = await db.getTemperatures();
  if (!temperatures) {
    return res.status(404);
  }
  return res.status(200).json({
    temperatures,
  });
};

export const getHumidityHandler: ExpressHandler<
  GetHumidityRequest,
  GetHumidityResponse
> = async (req, res) => {
  const humidities = await db.getHumedities();
  if (!humidities) {
    return res.status(404);
  }
  return res.status(200).json({
    humidities,
  });
};
