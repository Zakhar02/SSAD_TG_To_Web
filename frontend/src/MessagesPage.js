import Navbar from 'react-bootstrap/Navbar';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';

import 'bootstrap/dist/css/bootstrap.min.css';



const TopNavbar = () => {
  return <Navbar bg="light" variant="light" expand="lg" fixed="top">
    <Container>
      <Navbar.Brand href="#home">TG2WEB</Navbar.Brand>
      <Nav className="me-auto">
        <Form className="d-flex">
          <FormControl
            type="search"
            placeholder="Search"
            className="mr-2"
            aria-label="Search"
          />
          <Button variant="primary">Open Channel</Button>
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

const MessagesList = () => {
  const messages = [
    { text: "Тестовое сообщение из канала" },
    { text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent efficitur urna ligula, id convallis mi varius at. Morbi sagittis aliquet sapien ut pellentesque. Duis mauris eros, tempus eget lectus quis, aliquet sollicitudin ipsum. Morbi sit amet urna accumsan, eleifend massa sit amet, dignissim odio. Sed quis risus auctor, pretium diam ut, tempus quam." },
    { text: "Ещё одно сообщение" },
    { text: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur" },
    { text: "Nulla lacus dui, scelerisque a congue id, feugiat sed leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In in libero ac nisl suscipit pellentesque eget sit amet lorem. Nunc at velit fermentum, vulputate tortor blandit, congue turpis. Pellentesque et ante euismod lacus rhoncus viverra. Phasellus finibus neque odio, vel tristique nibh suscipit sit amet. Phasellus vestibulum eget sapien sit amet porta" }
  ];
  return <Container>
      <Row><br /></Row>
      {messages.map(({ text }) => <MessageItem text={text} />)}
      <Row><br /></Row>
    </Container>
};

const MessagesPage = () => {
  return <div>
    <TopNavbar />
    <MessagesList />
  </div>;
};

export default MessagesPage;