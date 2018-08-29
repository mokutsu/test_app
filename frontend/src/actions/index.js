import axios from 'axios';
const ROOT_URL = `'https://api.coindesk.com/v1/bpi/currentprice.json'`

export const FETCH_WEATHER = 'FETCH_WEATHER';
// this function fetches weather from the open weather map API and returns the payload using axios
export function fetchWeather(cityName) {
  const url = `${ROOT_URL}`
  const request = axios.get(url);
  console.log('request: ', request);

  return {
    type: FETCH_WEATHER,
    payload: request // we are returning the promise as the payload but redux promise handles the promise for us and resolves it
  };
}
