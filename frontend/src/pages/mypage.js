import axios from 'axios';

function MyPage({ data }) {
  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}

export async function getServerSideProps(context) {
  const response = await axios.get('http://localhost:8000/api/data/');
  return {
    props: {
      data: response.data
    }
  };
}

export default MyPage;
