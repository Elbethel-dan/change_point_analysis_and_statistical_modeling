import React from "react";

function Filters({ setRange }) {
  return (
    <div style={{ marginBottom: 20 }}>
      <input
        type="date"
        onChange={(e) =>
          setRange(prev => ({ ...prev, start: e.target.value }))
        }
      />
      <input
        type="date"
        onChange={(e) =>
          setRange(prev => ({ ...prev, end: e.target.value }))
        }
      />
    </div>
  );
}

export default Filters;
