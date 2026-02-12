import axios from "axios";

const API = "http://localhost:5000/api";

export const fetchPrices = (start, end) =>
  axios.get(`${API}/prices`, { params: { start, end } });

export const fetchChangePoint = () =>
  axios.get(`${API}/changepoint`);

export const fetchEvents = () =>
  axios.get(`${API}/events`);

export const fetchVolatility = () =>
  axios.get(`${API}/volatility`);
