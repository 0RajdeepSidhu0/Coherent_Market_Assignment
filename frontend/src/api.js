// src/api.js

const BASE_URL = "https://coherent-market-assignment-h7ah.vercel.app";

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