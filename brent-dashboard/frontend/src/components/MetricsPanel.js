import React from "react";

function MetricsPanel({ cp }) {
  const percentShift =
    ((Math.exp(cp.mu_2) - Math.exp(cp.mu_1)) * 100).toFixed(2);

  return (
    <div style={{ marginTop: 20 }}>
      <h3>Change Point Metrics</h3>
      <p>Change Date: {cp.change_date}</p>
      <p>Mean Before: {cp.mu_1}</p>
      <p>Mean After: {cp.mu_2}</p>
      <p>Estimated % Shift: {percentShift}%</p>
      <p>Volatility (σ): {cp.sigma}</p>
    </div>
  );
}

export default MetricsPanel;
