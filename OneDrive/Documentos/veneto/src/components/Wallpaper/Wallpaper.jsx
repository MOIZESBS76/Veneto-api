import React, { useState } from "react";
import "./Wallpaper_estrutura.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

function Wallpaper() {
  const [open, setOpen] = useState(false);

  function toggleOpen() {
    setOpen((prev) => !prev);
  }

  return (
    <div className="wallpaper">
      <img className="wallpaper-image" src="/img/wallpape_veneto_logo.jpg" alt="Logo Wallpaper" />

      <div className="coluna-tempopreparo-vermais">
        <div className="tempo-preparo">
          <i className="fa-solid fa-clock"></i>
          <p className="minutos"> 80 - 90 minutos </p>
        </div>
        <button className="botao-vermais"> Ver Mais </button>
      </div>

      <div className="coluna-aval-bot">

        <div className="avaliacao">
          <p className="nota-avaliacao"> 4.8 </p>
          <i className="fa-solid fa-star"></i>
          <p className="total-avaliacoes"> (200+) </p>
        </div>

        <button className={`botao-fechado-aberto ${open ? "aberto" : "fechado"}`} onClick={toggleOpen} aria-pressed={open}>
          {open ? "Aberto para pedidos" : "Fechado para pedidos"}
        </button>
        
      </div>

    </div>
  );
}

export default Wallpaper;