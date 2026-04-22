import { useEffect, useState } from "react";
import {
  getStartups,
  searchStartups,
  getStartup,
  getRecommendations,
} from "./api";

import SearchBar from "./components/SearchBar";
import StartupList from "./components/StartupList";
import StartupDetail from "./components/StartupDetail";
import "./App.css";

function App() {
  const [startups, setStartups] = useState([]);
  const [selected, setSelected] = useState(null);
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    loadStartups();
  }, []);

  const loadStartups = async () => {
    const res = await getStartups();
    setStartups(res.data);
  };

  const handleSearch = async (query) => {
    const res = await searchStartups(query);
    setStartups(res);
  };

  const handleSelect = async (slug) => {
    const startup = await getStartup(slug);
    const recs = await getRecommendations(slug);

    setSelected(startup);
    setRecommendations(recs.recommendations);
  };

  

  return (
    // <div>
    //   <h1>Startup Explorer</h1>

    //   <SearchBar onSearch={handleSearch} />

    //   <StartupList startups={startups} onSelect={handleSelect} />

    //   <StartupDetail
    //     startup={selected}
    //     recommendations={recommendations}
    //   />
    // </div>

  <div className="container">
    <h1 className="title">Startup Explorer</h1>

    <SearchBar onSearch={handleSearch} />

    <div className="layout">
      <StartupList startups={startups} onSelect={handleSelect} />

      <StartupDetail
        startup={selected}
        recommendations={recommendations}
      />
    </div>
  </div>
  );
}

export default App;