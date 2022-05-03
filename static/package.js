const url={
    "develop":{
        "url_api_message":"http://127.0.0.1:4000/api/message"
    },
    "production":{
        "url_api_message":"http://"+aws_url2+":4000/api/message"
    }
}

const aws_url="3.115.234.130";
const aws_url2="172.31.14.238";

// const env="develop";
const env="production";
export const url_mode=url[env];

export default url_mode;