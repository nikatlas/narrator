import { createAsyncThunk } from "@reduxjs/toolkit";

export type FetcherState<DataType> = {
  data: DataType | undefined;
  loading: boolean;
  status: "idle" | "loading" | "succeeded" | "failed";
  error: any;
};

export const fetcherInitialState: FetcherState<any> = {
  data: [],
  loading: false,
  status: "idle",
  error: null,
};

class Fetcher<Payload, FetcherResponse, ProcessedPayload, ProcessedData> {
  readonly name: string;
  protected fetchFn: (payload: ProcessedPayload) => Promise<FetcherResponse>;
  protected preparePayloadFn:
    | ((values: Payload) => Promise<ProcessedPayload>)
    | undefined;
  protected processDataFn:
    | ((
        data: FetcherResponse,
        state: FetcherState<FetcherResponse>,
        action: any,
      ) => ProcessedData)
    | undefined;
  private _thunk: any;

  constructor(
    name: string,
    fetchFn: (payload: ProcessedPayload) => Promise<FetcherResponse>,
    processData?: (
      data: FetcherResponse,
      state: FetcherState<FetcherResponse>,
      action: any,
    ) => ProcessedData,
    preparePayload?: (values: Payload) => Promise<ProcessedPayload>,
  ) {
    this.name = name;
    this.fetchFn = fetchFn;
    this.preparePayloadFn = preparePayload;
    this.processDataFn = processData;
  }

  thunk() {
    if (this._thunk) {
      return this._thunk;
    }
    this._thunk = createAsyncThunk(this.name, async (values: Payload) => {
      const payload = await this.preparePayload(values);
      const data = await this.fetch(payload);
      return { data, payload };
    });
    return this._thunk;
  }

  async preparePayload(values: Payload): Promise<ProcessedPayload> {
    if (this.preparePayloadFn) {
      return this.preparePayloadFn(values);
    }
    const processedValues: ProcessedPayload = values as any;
    return Promise.resolve(processedValues);
  }

  async fetch(payload: ProcessedPayload): Promise<FetcherResponse> {
    return this.fetchFn(payload);
  }
  processData(
    data: FetcherResponse,
    state: FetcherState<FetcherResponse>,
    action: any,
  ): ProcessedData {
    if (this.processDataFn) {
      return this.processDataFn(data, state, action);
    }
    return data as any;
  }

  reducers(builder: any) {
    const thunk = this.thunk();
    builder.addCase(thunk.pending, (state: any) => {
      state.loading = true;
      state.status = "loading";
    });
    builder.addCase(thunk.fulfilled, (state: any, action: any) => {
      state.loading = false;
      state.status = "succeeded";
      state.data = this.processData(action.payload.data, state, action.payload);
      state.error = null;
    });
    builder.addCase(thunk.rejected, (state: any, action: any) => {
      state.loading = false;
      state.status = "failed";
      state.error = action.error;
    });
  }

  get action() {
    return this.thunk();
  }
}

export default Fetcher;
