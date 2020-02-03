// frontend\src\modules\notification\notificationStore.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) 
const store = {
    
    state: {
        isSnackbarVisible: false
    },
    mutations: {
        setIsSnackbarVisible(state, isVisible){
            state.isSnackbarVisible = isVisible;
        },
    },
    actions: {
        setSnackbarVisibility({commit}, isVisible){
            commit('setIsSnackbarVisible', isVisible);
        },
        toggleSnackBarvisibleAction: {
            root: true,
            handler ({commit}) { 
                
                commit('setIsSnackbarVisible', true);
                setTimeout((c) => {
                    c('setIsSnackbarVisible', false);
                }, 15000, commit);
             }
        },
        
    },
    getters: {
        GetIsSnackbarVisible(state){
             return state.isSnackbarVisible;   
        }
    }
}

export default store;