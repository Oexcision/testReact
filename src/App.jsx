import React from 'react';
import LoginForm from './components/LoginForm';
import './styles/styles.css'; 

const App = () => {
  const handleLogin = (userData) => {
    // Lógica de autenticación, por ejemplo, enviar a un servidor
    console.log('Login data:', userData);
  };

  return (
    <div>
      <h1>Logueate al Puticlub de Zurdo</h1>
      <LoginForm onSubmit={handleLogin} />
    </div>
  );
};

export default App;