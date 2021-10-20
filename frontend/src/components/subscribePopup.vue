<template>
  <div>
    <div id="button-wrapper">
      <button @click="handleSubscriptionScreen" id="subscribe-button">Subscribe!</button>
    </div>
    <transition name="fade">
      <div id="subscription-screen-wrapper" v-if="screenOpened">
        <div id="subscription-screen">
          <img id="close-button" @click="handleSubscriptionScreen" src="@/assets/img/close_x.png">
          <div id="left-block">
            <h1 id="discount-text">10%<span>off</span></h1>
            <h3>for your first order</h3>
            <hr>
            <span id="explanation-text">Subscribe to recieve 10% off promo code abs<br> exclusive offers and deals</span>

            <form id="subscribe-form" @submit="submitSubscription">
              <label for="email">Email</label>
              <input v-model="email" id="email" type="email" required>
              <button type="submit">Subscribe!</button>
              <span id="submit-message" v-if="success" style="color: #138418">You have successfully subscribed to the newsletter</span>
              <span id="submit-message" v-if="fail" style="color: rgb(237 25 25);">You have already subscribed to the newsletter</span>
            </form>
          </div>
          <div id="right-block">
            <div id="purple-background"></div>
            <img id="banner" src="@/assets/img/subscription_image.png">
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'subscribePopup',

  data() {
    return {
      screenOpened: false,
      email: '',
      success: false,
      fail: false,
    }
  },

  methods: {
    handleSubscriptionScreen: function() {
      this.screenOpened = !this.screenOpened;
    },

    submitSubscription: async function(e) {
      e.preventDefault()
      this.success = false;
      this.fail = false;

      try {
        let resp = await axios.post(
          "http://localhost:8000/api/email-subscription/",
          {"email": this.email}
        )
        if(resp.status == 201) {
          this.success = true;
        }
      } catch {
        this.fail = true;
      }
    }
  }
}
</script>

<style scoped>
#button-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100vw;
  height: 100vh;
}

#subscribe-button {
  display: inline-block;

  background-color: #C24DFE;
  color: #FFFFFF;

  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 14px;
  line-height: 14px;

  letter-spacing: 2.5px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.6s ease 0s;
  cursor: pointer;
  outline: none;

  padding: 13px 60px;
  border-radius: 35px;
  border: 1px;
}

#subscribe-button:hover {
  background-color: #2F3639;
  box-shadow: 0px 15px 20px rgba(252, 40, 252, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

#subscription-screen-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;

  background-color: rgba(0, 0, 0, 0.35);

  position: fixed;
  top: 0;

}

#subscription-screen {
  display: flex;
  width: 100%;
  justify-content: space-between;

  position: relative;
  width: 864px;
  height: 502px;

  background-color: #FFFFFF;
  box-shadow: 0px 8px 20px rgba(68, 75, 77, 0.15);
  border-radius: 8px;

  overflow: hidden;
}

#purple-background {
  background-color: #C24DFE;

  height: 100%;
  width: 100%;
  z-index: 7;
  -webkit-clip-path: polygon(0 0, 85% 0, 94% 36%, 100% 100%, 16% 100%, 2% 45%);
  clip-path: polygon(0 0, 85% 0, 94% 36%, 100% 100%, 16% 100%, 2% 45%);
  
}

#banner {
  top: 0;
  right: 0;
  z-index: 10;
  position: absolute;

  -webkit-clip-path: polygon(8% 0, 83% 0, 100% 42%, 100% 100%, 51% 100%);
  clip-path: polygon(8% 0, 83% 0, 100% 42%, 100% 100%, 51% 100%);
}

#close-button {
  position: absolute;
  right: 10px;
  top: 10px;

  cursor: pointer;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

#left-block, #right-block {
  width: 50%;
}

#discount-text {
  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 104px;
  line-height: 100%;

  color: #2F3639;
}

#discount-text span {
  font-size: 20px;
}

#left-block h1, h3 {
  margin: 0;
}

#left-block {
  padding: 35px;
}

#left-block h3 {
  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 100%;

  color: #828688;
}

#left-block hr {
  width: 67px;
  height: 2px;

  background: #C24DFE;
  border-radius: 10px;

  margin: 26px 0px;
}

#explanation-text {
  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 120%;

  display: flex;
  align-items: center;

  color: #595E61;
}

#subscribe-form {
  margin-top: 40px;

  display: flex;
  flex-direction: column;
}

#subscribe-form label{
  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 12px;
  line-height: 14px;

  margin-top: -15px;
  margin-bottom: 20px;

  color: #828688;
}

#subscribe-form #email {
  background: #FFFFFF;
  width: 70%;
  height: 40px;
  padding: 7px;

  border: 1px solid #D5D7D7;
  box-sizing: border-box;
  border-radius: 6px;
  
  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 12px;
  line-height: 14px;
}

#subscribe-form button {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  padding: 13px 82px;
  text-align: center;

  position: static;
  width: 86px;
  height: 40px;
  margin-top: 15px;

  background: #C24DFE;
  border-radius: 35px;
  border: 1px;

  font-family: 'Roboto', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 14px;
  line-height: 14px;
  display: flex;
  align-items: center;
  text-align: center;

  color: #FFFFFF;
  cursor: pointer;
  transition: all 0.4s ease;
}

#subscribe-form button:hover {
  box-shadow: 0px 15px 20px rgba(252, 40, 252, 0.4);
}

#submit-message {
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 11px;
  margin-top: 15px;

  display: flex;
  align-items: center;

}
</style>