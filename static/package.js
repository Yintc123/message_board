const dn="message-board.yin888.info";
const ip="3.115.234.130:4000";
const lb="loadtestALB-817074138.ap-northeast-1.elb.amazonaws.com";

const url={
    "develop":{
        "url_api_message":"http://127.0.0.1:4000/api/message"
    },
    "production":{
        "url_api_message":"https://"+lb+"/api/message"
    }
}


// const env="develop";
const env="production";
export const url_mode=url[env];

export default url_mode;