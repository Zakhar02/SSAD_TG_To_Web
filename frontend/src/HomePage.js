import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

import 'bootstrap/dist/css/bootstrap.min.css';

import {
  useHistory,
} from "react-router-dom";



const ChannelNameForm = () => {
  const history = useHistory();

  const onSubmit = (e) => {
    e.preventDefault();

    const channelId = e.target.elements['channelId'].value;
    const url = `/channels/${channelId}/messages`;
    history.push(url, null);
  }

  return <Form onSubmit={onSubmit}>
    <Row className="align-items-center">
      <Col xs="auto">
        <Form.Label htmlFor="inlineFormInput" visuallyHidden>
          Telegram Channel Name
        </Form.Label>
        <Form.Control
          name="channelId"
          className="mb-2"
          id="inlineFormInput"
          placeholder="e.g. temablog"
        />
      </Col>
      <Col xs="auto">
        <Button type="submit" className="mb-2">
          Open channel
        </Button>
      </Col>
    </Row>
  </Form>;
};



const HomePage = () => {
  return <Container>
    <Row>
      <Col></Col>
      <Col style={{marginTop: 300}} xs={6}><ChannelNameForm /></Col>
      <Col></Col>
    </Row>
  </Container>;
};

export default HomePage;