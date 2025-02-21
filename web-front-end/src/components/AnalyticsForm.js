
import { Button, Form, Input} from 'antd';
import React, { useState } from 'react';
import { InputNumber } from "antd";
import face from '../img/face.jpeg'
import {Layout } from 'antd';
const { Header, Footer, Sider, Content } = Layout;

const siderStyle = {
  /*textAlign: 'center',
  lineHeight: '120px',
  color: '#fff',*/
  backgroundColor: '#FFFFFF',
};


const layout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      span: 26,
    },
  };

//const ip = "159.223.47.49"
const ip = "localhost"
// Define the original object 
const originalItem = {
  img_url: face,
  score: 0.9,
};
// Create an array with 10 copies of the original object
const imageArray = Array.from({ length: 20 }, () => ({ ...originalItem }));
const chunkArray = (array, chunkSize) => {
  const chunks = [];
  for (let i = 0; i < array.length; i += chunkSize) {
    chunks.push(array.slice(i, i + chunkSize));
  }
  return chunks;
};
 // Chunk the imageArray into sub-arrays of 5 images each
const chunkedImages = chunkArray(imageArray, 3);

const AnalyticsForm = ()=>{

    const [desc,setDesc] = useState('');
    const [k,setK] = useState(10);
    const [response, setResponse] = useState(null);
    const [rImageArray, setRImageArray] = useState(null)//useState(chunkedImages);
   
    const handleSubmit = (e) => {
      {/*e.preventDefault(); // Prevent form from refreshing the page*/}
      // Send GET request to Flask API with query parameters from form inputs
      const apiUrl = "http://"+ip+":5002/api/mmsys/query?desc="+desc+"&k="+k;
  
      fetch(apiUrl)
        .then((res) => res.json())
        .then((data) => 
          {
            const tmpImageArray = chunkArray(data,3);
            setRImageArray(tmpImageArray)//update array
            //alert(tmpImageArray[0][0].img_url)
            //setResponse(data)
         }) // Set response data to state
        .catch((error) => console.error('Error:', error));
    };


 

return (

<Layout>
  <Content style={siderStyle}>
  <Form
    {...layout}
    name="nest-messages"
    onFinish={handleSubmit}
    style={{
      maxWidth: '100%',
    }} 
  >
    <Form.Item name='desc'>
      <Input.TextArea  rows={12} value={desc} onChange={(e) => setDesc(e.target.value)} placeholder='Describe your images of interest'/>
    </Form.Item>
    <Form.Item
      wrapperCol={{
        ...layout.wrapperCol,
        offset: 8,
      }}
    >

   <Form.Item name='k'>
      <span>Number of matches (max:25) </span>
      <InputNumber min={1} max={25} value={k} onChange={(value) => setK(value)}/>
   </Form.Item>

      
      <Button type="primary" htmlType="submit">
        Submit
      </Button>
    </Form.Item>
  </Form>
  </Content>
  <Sider width='50%' style={siderStyle}>
  <div id="api_results">
   {
    rImageArray && (
      <div style={{paddingLeft: 20, paddingRight: 10, maxHeight: '400px', overflowY: 'auto'}}>
       {<table>
        <tbody>
          {rImageArray.map((imageRow, rowIndex) => (
            <tr key={rowIndex}>
              {imageRow.map((item, index) => (
                <td key={index} style={{ width: '30%' }}>
                  <img style={{ width: '100%' }} src={item.img_url} alt={`Image ${index + 1}`} />
                  <br />
                  Image {1+index + 3*(rowIndex)} {/*- Score: {item.score}*/}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
    </table>}
      </div>
    )
   }
  </div>
  </Sider>
</Layout>
)
}

export default AnalyticsForm;

