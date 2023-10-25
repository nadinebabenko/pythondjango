import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
class BuggyCounter extends Component {
  constructor(props) {
    super(props);
    this.state = { counter: 0 };
  }

  handleClick = () => {
    const { counter } = this.state;
    if (counter === 5) {
      throw new Error('I crashed!');
    }
    this.setState({ counter: counter + 1 });
  };

  render() {
    const { counter } = this.state;
    return <h1 onClick={this.handleClick}>{counter}</h1>;
  }
}

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { error: null, errorInfo: null };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ error, errorInfo });
  }

  render() {
    const { error, errorInfo } = this.state;
    if (error) {
      return (
        <div>
          <h2>Something went wrong.</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {error && error.toString()}
            <br />
            {errorInfo.componentStack}
          </details>
        </div>
      );
    }
    return this.props.children;
  }
}
export default App;
export { BuggyCounter, ErrorBoundary };


