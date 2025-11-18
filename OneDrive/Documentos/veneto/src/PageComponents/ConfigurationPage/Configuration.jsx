import React from "react";
import "./Configuration.estrutura.css";
import Header from "../../components/Header/Header";
import Wallpaper from "../../components/Wallpaper/Wallpaper";
import NavBar from "../../components/NavBar/NavBar";
import Footer from "../../components/Footer/Footer";

export default function Configuration() {
  return (
    <div className="home">
      <Header />
      <Wallpaper />
      <NavBar />

      <main>
        <h2>teste</h2>
      </main>

      <Footer />
    </div>
  );
}