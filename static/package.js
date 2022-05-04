const url={
    "develop":{
        "url_api_message":"http://127.0.0.1:4000/api/message"
    },
    "production":{
        "url_api_message":"http://3.115.234.130:4000/api/message"
    }
}


// const env="develop";
const env="production";
export const url_mode=url[env];

export default url_mode;