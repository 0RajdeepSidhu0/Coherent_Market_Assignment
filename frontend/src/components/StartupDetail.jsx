export default function StartupDetail({ startup, recommendations }) {
  if (!startup) return <div>Select a startup</div>;

  return (
    <div className="detail">
      <h2>{startup.name}</h2>

      <a href={startup.link} target="_blank">
        Visit Website
      </a>

      <h3 style={{ marginTop: "20px" }}>Recommended</h3>

      {recommendations.map((r) => (
        <div key={r.slug} className="card">
          {r.name}
        </div>
      ))}
    </div>
  );
}