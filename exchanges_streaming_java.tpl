package exchanges;

import org.knowm.xchange.ExchangeFactory;
import org.knowm.xchange.{{name}}.{{Name}}Exchange;

import info.bitrich.xchangestream.{{name}}.{{Name}}StreamingExchange;
import info.bitrich.xchangestream.core.StreamingExchangeFactory;

public class {{Name}} extends GenericStreamingExchange {
	public {{Name}}() {
		this.exchange = ExchangeFactory.INSTANCE.createExchange({{Name}}Exchange.class.getName());
		this.streamingExchange = StreamingExchangeFactory.INSTANCE
				.createExchange({{Name}}StreamingExchange.class.getName());
	}
}
