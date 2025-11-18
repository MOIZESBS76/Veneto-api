import React from "react";
import "./Header_estrutura.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import { useNavigate } from 'react-router-dom'

function Header() {

  const navigate = useNavigate()

  return (
    <div className="header">
      <div className="endereco">
        <div className="endereco-txt">Escolha um endereço</div>
        <div className="endereco-setaup">
          <i className="fa-solid fa-caret-down"></i>
        </div>
      </div>

      <div className="icons">
        <div className="icon-pesquisar">
          <i className="fa-solid fa-magnifying-glass" ></i>
        </div>

        <div className="icon-home">
          <i className="fa-solid fa-house" onClick={() => navigate('/home')}></i>
        </div>

        <div className="icon-profile">
          <i className="fa-solid fa-user" onClick={() => navigate('/profile')}></i>
        </div>

        <div className="icon-config">
          <i className="fa-solid fa-gear" onClick={() => navigate('/configurations')}></i>
        </div>

        <div className="icon-reservations">
          <i className="fa-solid fa-pen-to-square" onClick={() => navigate('/reservation')}></i>
        </div>

        <div className="icon-cart">
          <i className="fa-solid fa-cart-shopping" onClick={() => navigate('/cart')}></i>
          <span className="valor">00,00</span>
        </div>
      </div>
    </div>
  );
}

export default Header;
