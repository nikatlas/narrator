import axios, { AxiosResponse } from "axios";

export interface APIHeaders {
  [key: string]: string;
}

export default class HttpAPI {
  api: any;

  resource: string = "";

  constructor(BASE_URL: string = "", baseHeaders: APIHeaders = {}) {
    const api = axios.create({
      baseURL: BASE_URL,
      headers: baseHeaders,
    });

    this.api = api;
  }

  // eslint-disable-next-line
  getHeaders(): APIHeaders {
    return {};
  }

  // eslint-disable-next-line
  handleResponse<T>(response: AxiosResponse): T {
    if (response.status >= 200 && response.status <= 299) {
      return response.data as T;
    }
    throw response;
  }

  // eslint-disable-next-line
  handleError(error: Error): void {
    throw new Error(error.message);
  }

  async request<T>(
    method: string,
    url: string,
    data: any,
    config?: any,
  ): Promise<T> {
    const requestURL = this.resource + url;
    const requestConfig = {
      ...config,
      method,
      url: requestURL,
      data,
      headers: {
        ...this.getHeaders(),
        ...(config?.headers ?? {}),
      },
    };
    const responsePromise = this.api.request(requestConfig);
    return responsePromise
      .then((response: any) => this.handleResponse(response))
      .catch((err: any) => this.handleError(err));
  }

  get<T>(url: string, config?: any): Promise<T> {
    return this.request<T>("GET", url, null, config);
  }

  post<T>(url: string, data: any, config?: any): Promise<T> {
    return this.request<T>("POST", url, data, config);
  }

  put<T>(url: string, data: any, config?: any): Promise<T> {
    return this.request<T>("PUT", url, data, config);
  }

  patch<T>(url: string, data: any, config?: any): Promise<T> {
    return this.request<T>("PATCH", url, data, config);
  }

  delete(url: string, config?: any): Promise<Response> {
    return this.request("DELETE", url, null, config);
  }
}
