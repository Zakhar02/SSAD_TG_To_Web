import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import './App.css';

import HomePage from './HomePage.js';
import MessagesPage from './MessagesPage.js';



function App() {
  return <Router>
    <Switch>
      <Route path="/"><HomePage /></Route>
      <Route path="/channels/:channelId/messages"><MessagesPage /></Route>
    </Switch>
  </Router>;
}

export default App;
