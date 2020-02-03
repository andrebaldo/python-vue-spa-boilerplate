// frontend\src\store\index.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) 
import Vue from 'vue'
import Vuex from 'vuex'
import authStore from '@/modules/authentication/authStore'
import notificationStore from '@/modules/notification/notificationStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    authStore,
    notificationStore
  }
})
