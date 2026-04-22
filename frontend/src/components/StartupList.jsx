export default function StartupList({ startups, onSelect }) {
  return (
    <div className="list">
      <h3>Startups</h3>

      {startups.map((s) => (
        <div
          key={s.slug}
          onClick={() => onSelect(s.slug)}
          className="card"
        >
          <strong>{s.name}</strong>
          <div style={{ fontSize: "12px", color: "#666" }}>
            {s.source}
          </div>
        </div>
      ))}
    </div>
  );
}