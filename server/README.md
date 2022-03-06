# Server

This contains the list of all api endpoints and database configurations.

## API Endpoints

<details>
<summary>GET /readings/temp</summary>
<br>
get the temperature readings
<br><br>
<pre>
req body {
  "timestamp": "123456788" // time stamp of the last reading fetched (default: 0)
}
res body {
  "termperatures": [
    {
      "timestamp": "123456789",
      "temperature": "23.5"
    }
  ]
}
</pre>
</details>
<br>
<details>
<summary>GET /readings/humidity</summary>
<br>
get the humidity readings
<br><br>
<pre>
req body {
  "timestamp": "123456788" // time stamp of the last reading fetched (default: 0)
}
res body {
  "humidities": [
    {
      "timestamp": "123456789",
      "humidity": "70"
    }
  ]
}
</pre>
</details>
<br>
<details>
<summary>POST /reading</summary>
<br>
post a new reading
<br><br>
<pre>
req body {
  "timestamp": "123456789",
  "temperature": "23.5",
  "humidity": "70"
}
res body {}
</pre>
</details>
<br>
<details>
<summary>GET /control/alarm</summary>
<br>
get the alarm status
<br><br>
<pre>
req body {}
res body {
  "alarm": 1
}
</pre>
</details>
<br>
<details>
<summary>POST /control/alarm</summary>
<br>
post the alarm status
<br><br>
<pre>
req body {
  "is_set": 1
}
res body {}
</pre>
</details>
