import React from 'react';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import AnalyticsForm from './components/AnalyticsForm';

const { Header, Content, Footer } = Layout;
const items = [{key:"1", label:"Home"}, {key:"2", label:"About Us"}]
/*
const items = new Array(1).fill(null).map((_, index) => ({
  key: index + 1,
  label: `nav ${index + 1}`,
}));
*/

const institution_name = "Standard Bank"

const Home = function(){
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  return (
    <Layout>
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <div className="demo-logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['1']}
          items={items}
          style={{
            flex: 1,
            minWidth: 0,
          }}
        />
      </Header>


      <Content
        style={{
          padding: '0 48px',
        }}
      >
        <Breadcrumb
          style={{
            margin: '16px 0',
          }}
        >
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item> {institution_name} Multimodal Case Study Design</Breadcrumb.Item>
        </Breadcrumb>
        <div
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
        
       <AnalyticsForm/>


        </div>
      </Content>

      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Copyright ©{new Date().getFullYear()} Created by <a href="https://scholar.google.com/citations?user=J-QSVikAAAAJ&hl=en&oi=ao" target='_blank'>Yves Matanga</a> 
      </Footer>

    </Layout>
    
  );
};
export default Home;


{/*
    <Layout>
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <div className="demo-logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['1']}
          items={items}
          style={{
            flex: 1,
            minWidth: 0,
          }}
        />
      </Header>

      <Content
        style={{
          padding: '0 48px',
        }}
      >
        <Breadcrumb
          style={{
            margin: '16px 0',
          }}
        >
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item> {institution_name} Course Recommender App</Breadcrumb.Item>
        </Breadcrumb>
        <div
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
        
        <AnalyticsForm/>


        </div>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Copyright ©{new Date().getFullYear()} Created by <a href="https://bansoanalytics.com/" target='_blank'>Yves Matanga</a> 
      </Footer>
    </Layout>  */}