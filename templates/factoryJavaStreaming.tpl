package exchanges.factories;

import exchanges.factories.EntryPoint.Exchanges;

public class {{Name}}Factory extends GenericStreamingFactory {

	{{Name}}Factory() {
		exchange = Exchanges.{{NAME}};
		ticker_pub = "{{NAME}}_TICKER_PUB";
		orderbook_pub = "{{NAME}}_ORDERBOOK_PUB";
	}
}