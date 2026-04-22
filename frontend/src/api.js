// src/api.js
const BASE_URL = "http://127.0.0.1:8000";

export const getStartups = async () => {
  const res = await fetch(`${BASE_URL}/startups`);
  return res.json();
};

export const searchStartups = async (query) => {
  const res = await fetch(`${BASE_URL}/search?query=${query}`);
  return res.json();
};

export const getStartup = async (slug) => {
  const res = await fetch(`${BASE_URL}/startups/${slug}`);
  return res.json();
};

export const getRecommendations = async (slug) => {
  const res = await fetch(`${BASE_URL}/recommend/${slug}`);
  return res.json();
};