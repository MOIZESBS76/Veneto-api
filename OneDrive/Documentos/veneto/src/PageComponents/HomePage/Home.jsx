import React from "react";
import "./Home.css";
import Header from "../../components/Header/Header";
import Wallpaper from "../../components/Wallpaper/Wallpaper";
import NavBar from "../../components/NavBar/NavBar";
import Footer from "../../components/Footer/Footer";

export default function Home() {
  return (
    <div className="home">
      <Header />
      <Wallpaper />
      <NavBar />

      <main>
        <h2>Home Page</h2>
        <p>This is the home page of the Veneto application.</p>
      </main>

      <Footer />
    </div>
  );
}

