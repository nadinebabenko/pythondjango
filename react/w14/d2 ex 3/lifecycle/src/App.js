import React, { Component } from 'react';


class Child extends Component {
  componentWillUnmount() {
    alert('Component is unmounted');
  }

  render() {
    return <h1>Hello World!</h1>;
  }
}

class App extends Component {
  state = {
    show: true
  };

  handleDelete = () => {
    this.setState({ show: false });
  };

  render() {
    const { show } = this.state;

    return (
      <div>
        {show && <Child />}
        <button onClick={this.handleDelete}>Delete</button>
      </div>
    );
  }
}

export default App;