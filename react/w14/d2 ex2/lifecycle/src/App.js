import logo from './logo.svg';
import './App.css';
import React from 'react';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteColor: 'red'
    };
  }

  shouldComponentUpdate() {
    return true;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log("in getSnapshotBeforeUpdate");
    return null;
  }

  componentDidUpdate() {
    console.log("after update");
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            My favorite color is {this.state.favoriteColor}
          </p>
          <button onClick={() => this.setState({favoriteColor: 'blue'})}>
            Change color to blue
          </button>
        </header>
      </div>
    );
  }
}

export default App;