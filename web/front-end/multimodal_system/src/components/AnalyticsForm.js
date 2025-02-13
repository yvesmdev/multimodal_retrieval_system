
import { Button, Form, Input } from 'antd';
import React, { useState } from 'react';

const layout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      span: 16,
    },
  };
  
const AnalyticsForm = ()=>{

    const [desc,setDesc] = useState('');
    const [response, setResponse] = useState(null);
  
    const handleSubmit = (e) => {
      {/*e.preventDefault(); // Prevent form from refreshing the page*/}
      // Send GET request to Flask API with query parameters from form inputs
      const apiUrl = "http://127.0.0.1:5000/api/crapp/query?desc="+desc;
  
      fetch(apiUrl)
        .then((res) => res.json())
        .then((data) => setResponse(data)) // Set response data to state
        .catch((error) => console.error('Error:', error));
    };

return (
<div>
   <Form
    {...layout}
    name="nest-messages"
    onFinish={handleSubmit}
    style={{
      maxWidth: 900,
    }} 
  >
    <Form.Item name='desc'>
      <Input.TextArea  rows={12} value={desc} onChange={(e) => setDesc(e.target.value)} placeholder='Describe your image of interest'/>
    </Form.Item>
    <Form.Item
      wrapperCol={{
        ...layout.wrapperCol,
        offset: 8,
      }}
    >
      <Button type="primary" htmlType="submit">
        Submit
      </Button>
    </Form.Item>
  </Form>
  <div id="api_results">
   {
    response && (
        <p>{response.message}</p>
    )
   }
   { /* results of API matching! */}
  </div>
  </div>
)
}

export default AnalyticsForm;

