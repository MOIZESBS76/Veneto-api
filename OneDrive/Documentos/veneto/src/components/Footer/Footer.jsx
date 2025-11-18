import React from "react";
import "./Footer_estrutura.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

function Footer() {
  return(
    <div className="footer">
      <div className="obs">
        <h1 className="footer-titulo">Veneto</h1>

        <div className="row">
          <p className="footer-link">Avalie-nos</p> | <p className="footer-link">Conta e Segurança</p> | <p className="footer-link">Fale Conosco</p>
        </div>
      </div>

      <div className="rede-sociais">
        <h1 className="footer-titulo">Redes Sociais</h1>

        <div className="row-icones">
          <i className="fab fa-whatsapp"></i>
          <i className="fab fa-facebook"></i>
          <i className="fab fa-instagram"></i>
        </div>
      </div>

      <div className="terceira">
        <div className="lof-fo" >
          <img className="logo-footer" src="/img/logo_erased.png" alt="Veneto Logo"></img>
        </div>

        <div className="row">
          <p className="termos">Termos de Uso</p> | <p className="termos">Código de Conduta</p> | <p className="termos">Privacidade</p>
        </div>

        <div className="direitos-autorais">
          <p className="direitos-texto">© Copyright 2026 - RESTAURANTE E PIZZARIA VENETO DE MARICÁ LTDA. Todos os direitos reservados.</p>

          <p className="direitos-texto">CNPJ: 42.864.514/0001-35 / Endereço: Rod. Amaral Peixoto, km 22,5 - Maricá, Rio de Janeiro  CEP: 24942395</p>
        </div>
      </div>
    </div>
  );
}

export default Footer;