import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import FormControl from 'react-bootstrap/FormControl';

import 'bootstrap/dist/css/bootstrap.min.css';



const ChannelNameForm = () => {
  return <Form>
    <Row className="align-items-center">
      <Col xs="auto">
        <Form.Label htmlFor="inlineFormInput" visuallyHidden>
          Telegram Channel Name
        </Form.Label>
        <Form.Control
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