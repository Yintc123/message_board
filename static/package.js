const dn="message-board.yin888.info";
const ip="3.115.234.130:4000";
const lb="message-board1.yin888.info";

const url={
    "develop":{
        "url_api_message":"http://127.0.0.1:4000/api/message"
    },
    "production":{
        "url_api_message":"https://"+dn+"/api/message"
    }
}


// const env="develop";
const env="production";
export const url_mode=url[env];

export default url_mode;