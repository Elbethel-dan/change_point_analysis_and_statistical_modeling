import React, { useEffect, useState } from "react";
import { fetchPrices, fetchChangePoint, fetchEvents } from "./api";
import PriceChart from "./components/PriceChart";
import Filters from "./components/Filters";
import MetricsPanel from "./components/MetricsPanel";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [cp, setCp] = useState(null);
  const [range, setRange] = useState({ start: "", end: "" });

  useEffect(() => {
    fetchPrices(range.start, range.end).then(res => setPrices(res.data));
  }, [range]);

  useEffect(() => {
    fetchChangePoint().then(res => setCp(res.data));
    fetchEvents().then(res => setEvents(res.data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>Brent Oil Change Point Dashboard</h2>

      <Filters setRange={setRange} />

      <PriceChart
        prices={prices}
        events={events}
        changePoint={cp}
      />

      {cp && <MetricsPanel cp={cp} />}
    </div>
  );
}

export default App;
