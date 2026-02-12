import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ReferenceLine,
  ResponsiveContainer
} from "recharts";

function PriceChart({ prices, events, changePoint }) {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={prices}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="Price" dot={false} />

        {changePoint && (
          <ReferenceLine
            x={changePoint.change_date}
            stroke="red"
            label="Change Point"
          />
        )}
      </LineChart>
    </ResponsiveContainer>
  );
}

export default PriceChart;
