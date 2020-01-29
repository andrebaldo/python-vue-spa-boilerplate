import axios from "axios";
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000/',
    timeout: 30000
});

const authStore = {
    state: {
        isUserLoggedIn: false,
        isRegistrationProcessSucceed: false,
        registrationProcessMessage: '',
        isProcessing: false,
        loginToken: '',
        loginProcessMessage: '',
    },
    mutations: {
        setLogged(state, loginResult) {
            state.isUserLoggedIn = loginResult.success;
            state.loginToken = loginResult.token;
            state.loginProcessMessage = loginResult.message;
            if (loginResult.success) {
                sessionStorage.loginToken = loginResult.token;
            }else  {
                sessionStorage.removeItem("loginToken");
            }
        },
        setRegistrationStatus(state, result) {
            state.isRegistrationProcessSucceed = result.success;
            sessionStorage.isRegistrationProcessSucceed = result.success;
            state.registrationProcessMessage = result.message;
        },
        setIsProcessing(state, isProcessing) {
            state.isProcessing = isProcessing
        },
    },
    actions: {
        registerNewUser({ commit, dispatch }, payload) {
            commit('setIsProcessing', true);
            axiosInstance.post('register', payload)
                .then(function (response) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');
                    commit('setRegistrationStatus', { success: true, message: response.data.message });
                    
                })
                .catch(function (error) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');
                    if (typeof error != 'undefined' && typeof error.response != 'undefined') {
                        commit('setRegistrationStatus', { success: false, message: error.response.data.message });
                    }else{
                        commit('setRegistrationStatus', { success: false, message: error.message });
                    }
                });
        },
        getLoginToken({ commit, dispatch }, payload) {
            commit('setIsProcessing', true);
            axiosInstance.post('token', payload)
                .then(function (response) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');
                    commit('setLogged', { success: true, token: response.data.token});

                })
                .catch(function (error) {
                    commit('setIsProcessing', false);
                    dispatch('toggleSnackBarvisibleAction');

                    if (typeof error != 'undefined' && typeof error.response != 'undefined') {
                        commit('setLogged', { success: false, message: error.response.data.message });
                    }else{
                        commit('setLogged', { success: false, message: error.message });
                    }
                });
        },
        setSnackbarVisibility({commit}, isVisible){
            commit('setIsSnackbarVisible', isVisible);
        }
    },
    getters: {
        getIsRegistrationProcessSucceed(state) {
            if (state.registrationProcessMessage === '') {
                return undefined;
            } else {
                return state.isRegistrationProcessSucceed;
            }

        },
        getRegistrationProcessMessage(state) {
            return state.registrationProcessMessage;
        },
        getLoginProcessMessage(state) {
            return state.loginProcessMessage;
        },
        isProcessing(state) {
            return state.isProcessing;
        },
        isUserLoggedIn() {
            if (sessionStorage.loginToken) {
                return true;
            }
            return false;
        }
    }
}

export default authStore;