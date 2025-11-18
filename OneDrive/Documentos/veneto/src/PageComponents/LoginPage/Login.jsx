import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Login_estrutura.css";

export default function Login() {
  const [formData, setFormData] = useState({
    email: "",
    senha: "",
    lembrarDeMim: false,
  });
  const [mostrarSenha, setMostrarSenha] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    const emailArmazenado = localStorage.getItem("email");
    const lembrarDeMimArmazenado = localStorage.getItem("lembrarDeMim");
    
    if (emailArmazenado && lembrarDeMimArmazenado === "true") {
      setFormData((prevData) => ({
        ...prevData,
        email: emailArmazenado,
        lembrarDeMim: true,
      }));
    }
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.email || !formData.senha) {
      alert("Por favor, preencha todos os campos.");
      return;
    }
    
    if (formData.lembrarDeMim) {
      localStorage.setItem("email", formData.email);
      localStorage.setItem("lembrarDeMim", "true");
    } else {
      localStorage.removeItem("email");
      localStorage.removeItem("lembrarDeMim");
    }
    
    alert("Login realizado com sucesso!");
    navigate("/home");
  };

  return (
    <div className="login">
      <div className="papel-parede">
        <img
          className="logo-footer"
          src="/img/logo_erased.png"
          alt="Veneto Logo"
        />
      </div>

      <div className="formulario">
        <form onSubmit={handleSubmit}>
          <label htmlFor="email">
            <b> E-mail </b>
          </label>
          <input
            type="text"
            placeholder="Digite seu e-mail"
            name="email"
            required
            value={formData.email}
            onChange={handleChange}
          />

          <label htmlFor="senha">
            <b> Senha </b>
          </label>
          <div className="container-senha">
            <input
              type={mostrarSenha ? "text" : "password"}
              placeholder="Digite sua senha"
              name="senha"
              required
              value={formData.senha}
              onChange={handleChange}
            />
            <button
              type="button"
              className="botao-olho"
              onClick={() => setMostrarSenha(!mostrarSenha)}
              title={mostrarSenha ? "Ocultar senha" : "Mostrar senha"}
            >
              <i className={mostrarSenha ? "fas fa-eye" : "fas fa-eye-slash"}></i>
            </button>
          </div>

          <div className="lembrar-de-mim">
            <input
              type="checkbox"
              id="lembrarDeMim"
              name="lembrarDeMim"
              checked={formData.lembrarDeMim}
              onChange={handleChange}
            />
            <label htmlFor="lembrarDeMim">
              Lembrar de mim 
            </label>
          </div>

          <button className="botao-login" type="submit">
            Login
          </button>

          <div className="esqueci-senha">
            <a href="#"> Esqueci minha senha </a>
          </div>
        </form>
      </div>
    </div>
  );
}