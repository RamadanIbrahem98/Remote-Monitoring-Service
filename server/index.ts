import express, { ErrorRequestHandler, RequestHandler } from 'express';
import cors from 'cors';
import { initDb } from './database';
import {
  newEntryHandler,
  getTempHandler,
  getHumidityHandler,
  purgeHandler,
  getAlarmHandler,
  setAlarmHandler,
} from './handlers/sensorsHandler';

(async () => {
  await initDb();

  const app = express();

  app.use(express.json());
  app.use(cors());

  const requestLoggerMiddleware: RequestHandler = (req, res, next) => {
    console.log(req.method, req.path, '- body:', req.body);
    next();
  };

  app.use(requestLoggerMiddleware);

  app.post('/reading', newEntryHandler);

  app.get('/readings/temp', getTempHandler);

  app.get('/readings/humidity', getHumidityHandler);

  app.get('/readings/purge', purgeHandler);

  app.get('/control/alarm', getAlarmHandler);

  app.post('/control/alarm', setAlarmHandler);

  app.use('*', (req, res) => {
    res.status(404).json({
      message: 'Not found',
    });
  });

  const errHandler: ErrorRequestHandler = (err, req, res, next) => {
    console.error('Uncaught exception:', err);
    return res.status(500).json({
      message: 'Oops, an unexpected error occurred, please try again',
    });
  };
  app.use(errHandler);

  const port = process.env.PORT || 80;

  app.listen(port, () => console.log(`Listening on port ${port}`));
})();
