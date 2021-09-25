import React, { useState, useEffect } from 'react';

import Navbar from 'react-bootstrap/Navbar';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';

import 'bootstrap/dist/css/bootstrap.min.css';

import {
  useParams,
  useHistory,
} from "react-router-dom";



const TopNavbar = ({ initialChannelId }) => {
  const [channelId, updateChannelId] = useState(initialChannelId);

  const history = useHistory();

  const onSubmitOrClick = (e) => {
    e.preventDefault();

    const url = `/channels/${channelId}/messages`;
    history.push(url, null);
  }

  const onTextChange = (e) => {
    updateChannelId(e.target.value);
  };

  // highlight button, if value was changed
  const buttonVariant = (initialChannelId === channelId) ? null : "primary";

  return <Navbar bg="light" variant="light" expand="lg" fixed="top">
    <Container>
      <Navbar.Brand href="#home">TG2WEB</Navbar.Brand>
      <Nav className="me-auto">
        <Form onSubmit={onSubmitOrClick} className="d-flex">
          <FormControl
            type="search"
            placeholder="Search"
            className="mr-2"
            aria-label="Search"
            value={channelId}
            onChange={onTextChange}
          />
          <Button onClick={onSubmitOrClick} variant={buttonVariant}>Open Channel</Button>
        </Form>
      </Nav>
    </Container>
  </Navbar>;
};



const MessageItem = ({ text }) => {
  return <Row>
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Text>{text}</Card.Text>
      </Card.Body>
    </Card>
  </Row>;
};



const MessagesList = ({ messages }) => {
  if (messages === null) {
    return <div>Loading...</div>;
  }

  return <Container>
      <Row><br /></Row>
      {messages.map(({ text }, i) => <MessageItem key={i} text={text} />)}
      <Row><br /></Row>
    </Container>
};

const MessagesPage = () => {
  const { channelId } = useParams();

  const [messages, updateMessages] = useState(null);

  useEffect(() => {
    const url = `/api/channels/${channelId}/messages`;
    fetch(url)
      .then(resp => resp.json())
      .then(items => updateMessages(items));
  }, [channelId]);

  return <div>
    <TopNavbar initialChannelId={channelId} />
    <MessagesList messages={messages} />
  </div>;
};

export default MessagesPage;