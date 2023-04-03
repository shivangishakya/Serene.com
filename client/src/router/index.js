
/* eslint-disable */
import { createRouter, createWebHistory } from 'vue-router'

// Vue.config.productionTip = false;

import Homepage from "@/components/Homepage.vue";
import LoginModal from "@/components/LoginModal.vue";
import RegisterModal from "@/components/RegisterModal.vue";
import SurveyR from "@/components/SurveyR.vue";
import Result from "@/components/Result.vue";

const routes = [
    {
        path: "/",
        name: "Homepage",
        component: Homepage,
    },
    {
        path: "/login",
        name: "LoginModal",
        component: LoginModal,
    },
    {
        path: "/register",
        name: "RegisterModal",
        component: RegisterModal,
    },
    {
        path: "/survey",
        name: "SurveyR",
        component: SurveyR,
    },
    {
        path: "/result",
        name: "Result",
        component: Result,
    },
];

const router = createRouter({
history: createWebHistory(),
routes,
});

export default router;
